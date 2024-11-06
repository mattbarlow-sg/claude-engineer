from abc import ABC, abstractmethod

service_registry_response = {
    'UserService': {
        'url': 'http://user-service:8080',
        'version': '1.0.0',
        'status': 'healthy',
        'dependencies': ['AuthService'],
        'metadata': {
            'description': 'Handles user authentication and profiles',
            'maintainer': 'user-team@example.com'
        }
    },
    'VideoService': {
        'url': 'http://video-service:8080',
        'version': '2.1.3',
        'status': 'healthy',
        'dependencies': ['StorageService', 'EncodingService'],
        'metadata': {
            'description': 'Streams video content to users',
            'maintainer': 'video-team@example.com'
        }
    },
    'RecommendationService': {
        'url': 'http://recommendation-service:8080',
        'version': '1.2.5',
        'status': 'degraded',
        'dependencies': ['AnalyticsService'],
        'metadata': {
            'description': 'Provides content recommendations',
            'maintainer': 'reco-team@example.com'
        }
    },
    'PaymentService': {
        'url': 'http://payment-service:8080',
        'version': '3.0.1',
        'status': 'maintenance',
        'dependencies': ['BillingService'],
        'metadata': {
            'description': 'Processes user payments and subscriptions',
            'maintainer': 'payment-team@example.com'
        }
    },
}


class Registry(ABC):
    @abstractmethod
    def services(self, data: list) -> list:
        pass


# custom implementation
class ServiceLookupLocal(Registry):
    def services(self) -> map:
        return service_registry_response


# custom implementation
class ServiceLookupRemote(Registry):
    def execute(self, data: str) -> map:
        return {data: "test remote data"}


class Context:
    def __init__(self, registry: Registry):
        self._registry = registry

    def set_registry_strategy(self, registry: Registry):
        self._registry = registry

    def service_lookup(self) -> map:
        return self._registry.services()


# if __name__ == "__main__":
#     context = Context(ServiceLookupLocal())
#
#     print(context.service_lookup())
