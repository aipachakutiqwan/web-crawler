class RedisImagesNotFound(Exception):
    def __init__(self, message="Images not found in redis"):
        self.message = message
        super().__init__(self.message)


class OrchestratorOutputJsonReadingError(Exception):
    def __init__(self, message="Error reading Json from Orchestrator"):
        self.message = message
        super().__init__(self.message)


class RedisRetryException(Exception):
    def __init__(self, message="Redis Connection Not Available - Max number of retries reached"):
        self.message = message
        super().__init__(self.message)


class RedisCleanupError(Exception):
    def __init__(self, message="Error during redis cleanup"):
        self.message = message
        super().__init__(self.message)


class ExecuteQueryError(Exception):
    def __init__(self, message="Error during execute query"):
        self.message = message
        super().__init__(self.message)


class OnpremisDocUploaderServiceCallError(Exception):
    def __init__(self, message="Error calling onpremis doc uploader service"):
        self.message = message
        super().__init__(self.message)


class GcpBucketError(Exception):
    def __init__(self, message="Error in gcp bucket handler"):
        self.message = message
        super().__init__(self.message)
