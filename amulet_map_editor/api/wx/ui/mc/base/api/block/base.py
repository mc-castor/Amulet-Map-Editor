from typing import Optional

from ..resource_id import BaseMCResourceIDAPI, BaseMCResourceID


class BaseMCBlockAPI(BaseMCResourceIDAPI):
    pass


class BaseMCBlock(BaseMCResourceID, BaseMCBlockAPI):
    def set_namespace(self, namespace: Optional[str]):
        if namespace is None:
            self._namespace = self._translation_manager.get_version(
                self.platform, self.version_number
            ).block.namespaces(self.force_blockstate)[0]
        else:
            self._namespace = str(namespace)

    def set_base_name(self, base_name: Optional[str]):
        if base_name is None:
            blocks = self._translation_manager.get_version(
                self.platform, self.version_number
            ).block.base_names(self.namespace, self.force_blockstate)
            if blocks:
                self._block_name = blocks[0]
            else:
                self._block_name = ""
        else:
            self._block_name = str(base_name)
