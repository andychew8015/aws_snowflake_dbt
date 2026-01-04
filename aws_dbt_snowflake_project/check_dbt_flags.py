
import dbt.flags
import os

print(f"dbt version: {dbt.version.__version__}")

try:
    # Attempt to access standard flag locations
    print(f"Directory of dbt.flags: {dir(dbt.flags)}")
except Exception as e:
    print(f"Error inspecting dbt.flags: {e}")

try:
    print(f"default_profiles_dir: {dbt.flags.default_profiles_dir}")
except AttributeError:
    print("dbt.flags.default_profiles_dir does not exist as an attribute")
except NameError:
    print("default_profiles_dir is not defined (NameError)")

