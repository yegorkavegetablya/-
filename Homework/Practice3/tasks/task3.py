from Practice3.tasks.for_module.module_with_global_var import GLOBAL_VAR, f
GLOBAL_VAR = 42
f()

from Practice3.tasks.for_module import module_with_global_var
module_with_global_var.GLOBAL_VAR = 42
module_with_global_var.f()