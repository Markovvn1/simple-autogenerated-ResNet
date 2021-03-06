from pkg.module_builder import ModuleBuilderBase


class ModuleBuilder(ModuleBuilderBase):

	def __init__(self):
		super().__init__({"backbone.Backbone"})

	def _assert_cfg(self, module, cfg):
		assert not cfg

	def _dependencies(self, module, global_params, cfg):
		return {}

	def _init_file(self, dep):
		res = ", ".join([i[i.find(".")+1:] for i in dep.keys()])
		return "from .backbone import " + res

	def _generate(self, global_params, dep, childs):
		return _generate(global_params, dep)


def _generate(global_params, dep):
	return """\
import torch.nn as nn


class Backbone(nn.Module):

	\"\"\"
	Properties of class:
		in_channels (int): Количество каналов на входе
		out_strides (list[int]): Произведение всех stride до данного stage
		out_channels (list[int]): Количество каналов на данном stage
		out_features (list[str]): Непустой список stage'ей, которые должны
			быть возвращены после вызова forward. Отсортированный по
			порядку выполнения
		size_divisibility (int): разрешение входного слоя должно делиться на это число
	\"\"\"

	def __init__(self):
		super().__init__()		

	def _init(self, in_channels, out_features, out_channels, out_strides, size_divisibility=1):
		assert len(out_features) == len(out_channels) and len(out_channels) == len(out_strides)

		self.in_channels = in_channels
		self.out_features = out_features
		self.out_channels = out_channels
		self.out_strides = out_strides
		self.size_divisibility = size_divisibility

	def assert_input(self, x):
		assert x.dim() == 4 and x.size(1) == self.in_channels,\\
			f"Input shape have to be (N, {self.in_channels}, H, W). Got {x.shape} instead!"
		assert x.size(2) % self.size_divisibility == 0 and x.size(3) % self.size_divisibility == 0,\\
			f"Размеры входных изображений должны делиться на self.size_divisibility"\n"""