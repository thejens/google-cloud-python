# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.scheduler_v1.proto import (
    cloudscheduler_pb2 as google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2,
)
from google.cloud.scheduler_v1.proto import (
    job_pb2 as google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CloudSchedulerStub(object):
    """The Cloud Scheduler API allows external entities to reliably
  schedule asynchronous jobs.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.ListJobs = channel.unary_unary(
            "/google.cloud.scheduler.v1.CloudScheduler/ListJobs",
            request_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.ListJobsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.ListJobsResponse.FromString,
        )
        self.GetJob = channel.unary_unary(
            "/google.cloud.scheduler.v1.CloudScheduler/GetJob",
            request_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.GetJobRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.FromString,
        )
        self.CreateJob = channel.unary_unary(
            "/google.cloud.scheduler.v1.CloudScheduler/CreateJob",
            request_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.CreateJobRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.FromString,
        )
        self.UpdateJob = channel.unary_unary(
            "/google.cloud.scheduler.v1.CloudScheduler/UpdateJob",
            request_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.UpdateJobRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.FromString,
        )
        self.DeleteJob = channel.unary_unary(
            "/google.cloud.scheduler.v1.CloudScheduler/DeleteJob",
            request_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.DeleteJobRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.PauseJob = channel.unary_unary(
            "/google.cloud.scheduler.v1.CloudScheduler/PauseJob",
            request_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.PauseJobRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.FromString,
        )
        self.ResumeJob = channel.unary_unary(
            "/google.cloud.scheduler.v1.CloudScheduler/ResumeJob",
            request_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.ResumeJobRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.FromString,
        )
        self.RunJob = channel.unary_unary(
            "/google.cloud.scheduler.v1.CloudScheduler/RunJob",
            request_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.RunJobRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.FromString,
        )


class CloudSchedulerServicer(object):
    """The Cloud Scheduler API allows external entities to reliably
  schedule asynchronous jobs.
  """

    def ListJobs(self, request, context):
        """Lists jobs.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetJob(self, request, context):
        """Gets a job.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateJob(self, request, context):
        """Creates a job.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateJob(self, request, context):
        """Updates a job.

    If successful, the updated [Job][google.cloud.scheduler.v1.Job] is returned. If the job does
    not exist, `NOT_FOUND` is returned.

    If UpdateJob does not successfully return, it is possible for the
    job to be in an [Job.State.UPDATE_FAILED][google.cloud.scheduler.v1.Job.State.UPDATE_FAILED] state. A job in this state may
    not be executed. If this happens, retry the UpdateJob request
    until a successful response is received.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteJob(self, request, context):
        """Deletes a job.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PauseJob(self, request, context):
        """Pauses a job.

    If a job is paused then the system will stop executing the job
    until it is re-enabled via [ResumeJob][google.cloud.scheduler.v1.CloudScheduler.ResumeJob]. The
    state of the job is stored in [state][google.cloud.scheduler.v1.Job.state]; if paused it
    will be set to [Job.State.PAUSED][google.cloud.scheduler.v1.Job.State.PAUSED]. A job must be in [Job.State.ENABLED][google.cloud.scheduler.v1.Job.State.ENABLED]
    to be paused.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ResumeJob(self, request, context):
        """Resume a job.

    This method reenables a job after it has been [Job.State.PAUSED][google.cloud.scheduler.v1.Job.State.PAUSED]. The
    state of a job is stored in [Job.state][google.cloud.scheduler.v1.Job.state]; after calling this method it
    will be set to [Job.State.ENABLED][google.cloud.scheduler.v1.Job.State.ENABLED]. A job must be in
    [Job.State.PAUSED][google.cloud.scheduler.v1.Job.State.PAUSED] to be resumed.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RunJob(self, request, context):
        """Forces a job to run now.

    When this method is called, Cloud Scheduler will dispatch the job, even
    if the job is already running.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CloudSchedulerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListJobs": grpc.unary_unary_rpc_method_handler(
            servicer.ListJobs,
            request_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.ListJobsRequest.FromString,
            response_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.ListJobsResponse.SerializeToString,
        ),
        "GetJob": grpc.unary_unary_rpc_method_handler(
            servicer.GetJob,
            request_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.GetJobRequest.FromString,
            response_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.SerializeToString,
        ),
        "CreateJob": grpc.unary_unary_rpc_method_handler(
            servicer.CreateJob,
            request_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.CreateJobRequest.FromString,
            response_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.SerializeToString,
        ),
        "UpdateJob": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateJob,
            request_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.UpdateJobRequest.FromString,
            response_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.SerializeToString,
        ),
        "DeleteJob": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteJob,
            request_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.DeleteJobRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "PauseJob": grpc.unary_unary_rpc_method_handler(
            servicer.PauseJob,
            request_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.PauseJobRequest.FromString,
            response_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.SerializeToString,
        ),
        "ResumeJob": grpc.unary_unary_rpc_method_handler(
            servicer.ResumeJob,
            request_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.ResumeJobRequest.FromString,
            response_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.SerializeToString,
        ),
        "RunJob": grpc.unary_unary_rpc_method_handler(
            servicer.RunJob,
            request_deserializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_cloudscheduler__pb2.RunJobRequest.FromString,
            response_serializer=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.Job.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.scheduler.v1.CloudScheduler", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))