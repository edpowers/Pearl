# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import sys
import os

abs_file_path = os.path.abspath(__file__)
# Get the directory of the current script
abs_file_dir = os.path.dirname(abs_file_path)

# Get the parent directory of the current script's directory
parent_dir = os.path.dirname(abs_file_dir)

# Add the parent directory to sys.path
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from .pearl_agent import PearlAgent

__all__ = ["PearlAgent"]
