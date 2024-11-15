from abc import ABC, abstractmethod
import json
from typing import List, Dict, Optional, Any

with open('./data/services.json', 'r') as file:
    service_registry_response = json.load(file)

with open('./data/resources.json', 'r') as file:
    resource_inventory_response = json.load(file)


class Registry(ABC):
    @abstractmethod
    def services(self) -> Dict:
        pass

    @abstractmethod
    def resources(self, filter_criteria: Optional[str] = None) -> Dict:
        pass

    @abstractmethod
    def code(self, github_url: str) -> str:
        pass

# Custom implementation
class CustomerOneLookup(Registry):
    def services(self) -> Dict:
        return service_registry_response

    def resources(self, filter_criteria: Optional[str] = None) -> Dict:
        if filter_criteria:
            filtered_resources = {
                "resources": []
            }
            for resource_wrapper in resource_inventory_response.get("resources", []):
                resource = resource_wrapper.get("resource", {})
                if self._contains_value(resource, filter_criteria):
                    filtered_resources["resources"].append(resource_wrapper)
            return filtered_resources
        else:
            return resource_inventory_response

    def _contains_value(self, data: Any, search_value: str) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if self._contains_value(value, search_value):
                    return True
        elif isinstance(data, list):
            for item in data:
                if self._contains_value(item, search_value):
                    return True
        else:
            if search_value.lower() in str(data).lower():
                return True
        return False

    def code(self, github_url: str) -> str:
        parent_dir = "/Users/matt.barlow/CustomerOne"
        repo_name = github_url.rstrip("/").split("/")[-1]
        return f"{parent_dir}/{repo_name}"


# Example custom implementation
class CustomerTwoLookup(Registry):
    def services(self) -> List:
        return {"ServiceA": "Data1", "ServiceB": "Data2"}

    def resources(self) -> Dict:
        return {"Resource1": "Data1", "Resource2": "Data2"}

    def code(self, github_url: str) -> str:
        return "/some/directory/codepath"


class Context:
    def __init__(self, registry: Registry):
        self._registry = registry

    def set_registry_strategy(self, registry: Registry):
        self._registry = registry

    def service_lookup(self) -> List:
        return self._registry.services()

    def resource_lookup(self, filter_criteria: Optional[str] = None) -> Dict:
        return self._registry.resources(filter_criteria)

    def code_path(self, github_url: str) -> str:
        return self._registry.code(github_url)


if __name__ == "__main__":
    context = Context(CustomerOneLookup())
    print("All Services:")
    print(context.service_lookup())

    print("\nAll Resources:")
    print(context.resource_lookup())

    print("\nFiltered Resources:")
    print(context.resource_lookup(filter_criteria="Recommendation"))

    print("\nRepo Path:")
    print(context.code_path(github_url="https://github.com/mattbarlow-sg/claude-engineer"))
