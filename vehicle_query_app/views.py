import time
import logging

from django.http import JsonResponse

from rest_framework import views, permissions, status
from rest_framework.authentication import BasicAuthentication

from .models import VehicleDetail
from .serializers import VehicleDetailSerializer

from knox.views import LoginView as KnoxLoginView

logger = logging.getLogger('ViewLogger')


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]


class VehicleDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    GET_KEY = 'license-plate-number'

    def get(self, request):
        params = request.GET
        if self.GET_KEY not in params:
            return JsonResponse({'detail': f"'{self.GET_KEY}' should be given as param"},
                                status=status.HTTP_400_BAD_REQUEST)

        plate_number = params[self.GET_KEY]
        plate_number = plate_number.split('/')[0]
        user = request.user

        # Try exact match first
        st = time.time()
        vehicles = VehicleDetail.objects.filter(plate_number=plate_number)
        retrieve_elapsed = (time.time() - st) * 1000
        logger.debug(f'elapsed time for exact match: {retrieve_elapsed:.3f} ms')

        if vehicles.count() > 0:
            logger.info(f'exact match for {plate_number} by {user.username}')
            response = self.make_response(plate_number, True, retrieve_elapsed, vehicles)
            return response

        # If exact match fails, try partial match
        st = time.time()
        vehicles = VehicleDetail.objects.filter(plate_number__trigram_word_similar=plate_number)
        retrieve_elapsed = (time.time() - st) * 1000
        logger.debug(f'elapsed time for partial match: {retrieve_elapsed:.3f} ms')

        if vehicles.count() > 0:
            logger.info(f'partial match for {plate_number} by {user.username}')
            response = self.make_response(plate_number, False, retrieve_elapsed, vehicles)
            return response

        # If both exact and partial failed, no match
        logger.info(f'no match for {plate_number} by {user.username}')
        response = self.make_response(plate_number, False, retrieve_elapsed, vehicles)
        return response

    @staticmethod
    def make_response(plate_number: str, is_exact: bool, elapsed_time_ms: float, queries):
        serializer = VehicleDetailSerializer(queries, many=True)
        response = dict(plate_number=plate_number,
                        is_exact=is_exact,
                        count=queries.count(),
                        retrieve_elapsed_ms=elapsed_time_ms,
                        vehicle_details=serializer.data)
        return JsonResponse(response, safe=False)
