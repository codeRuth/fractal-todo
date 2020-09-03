from django.urls import path

from .views import BucketList, BucketDetail, TodoDetail, TodoBucketDetail, TodoDoneToggle

urlpatterns = [
    path("buckets/", BucketList.as_view(), name="bucket_list"),
    path("bucket/<int:id>", BucketDetail.as_view(), name="bucket_detail"),
    path("bucket/<int:id>/todos", TodoBucketDetail.as_view(), name="todo_bucket_detail"),
    path("todo/<int:id>", TodoDetail.as_view(), name="todo_detail"),
    path("todo/<int:id>/done", TodoDoneToggle.as_view(), name="todo_detail"),
]
