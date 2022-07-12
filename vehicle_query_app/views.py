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
        logger.info(f'plate number: {plate_number}')

        # TODO: 매치 종류, 카운트 로깅 (유저별, 전체)
        st = time.time()
        vehicles = VehicleDetail.objects.filter(plate_number=plate_number)
        count = vehicles.count()
        retrieve_elapsed = (time.time() - st) * 1000
        logger.info(f'elapsed time to retrieve VehicleDetail: {retrieve_elapsed:.3f} ms')

        is_exact = True
        serializer = VehicleDetailSerializer(vehicles, many=True)

        # TODO: exact match 실패 시 partial match 진행
        # is_exact = False

        response = dict(is_exact=is_exact,
                        count=count,
                        retrieve_elapsed_ms=retrieve_elapsed,
                        vehicle_details=serializer.data)
        return JsonResponse(response, safe=False)
