# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""This module is for SageMaker accept types."""
from __future__ import absolute_import
from typing import List, Optional

from sagemaker.jumpstart import artifacts, utils as jumpstart_utils


def retrieve_options(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> List[str]:
    """Retrieves the supported accept types for the model matching the given arguments.

    Args:
        region (str): The AWS Region for which to retrieve the supported accept types.
            Defaults to ``None``.
        model_id (str): The model ID of the model for which to
            retrieve the supported accept types. (Default: None).
        model_version (str): The version of the model for which to retrieve the
            supported accept types. (Default: None).
        tolerate_vulnerable_model (bool): True if vulnerable versions of model
            specifications should be tolerated (exception not raised). If False, raises an
            exception if the script used by this version of the model has dependencies with known
            security vulnerabilities. (Default: False).
        tolerate_deprecated_model (bool): True if deprecated models should be tolerated
            (exception not raised). False if these models should raise an exception.
            (Default: False).
    Returns:
        list: The supported accept types to use for the model.

    Raises:
        ValueError: If the combination of arguments specified is not supported.
    """
    if not jumpstart_utils.is_jumpstart_model_input(model_id, model_version):
        raise ValueError(
            "Must specify JumpStart `model_id` and `model_version` when retrieving accept types."
        )

    return artifacts._retrieve_supported_accept_types(
        model_id,
        model_version,
        region,
        tolerate_vulnerable_model,
        tolerate_deprecated_model,
    )


def retrieve_default(
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> str:
    """Retrieves the default accept type for the model matching the given arguments.

    Args:
        region (str): The AWS Region for which to retrieve the default accept type.
            Defaults to ``None``.
        model_id (str): The model ID of the model for which to
            retrieve the default accept type. (Default: None).
        model_version (str): The version of the model for which to retrieve the
            default accept type. (Default: None).
        tolerate_vulnerable_model (bool): True if vulnerable versions of model
            specifications should be tolerated (exception not raised). If False, raises an
            exception if the script used by this version of the model has dependencies with known
            security vulnerabilities. (Default: False).
        tolerate_deprecated_model (bool): True if deprecated models should be tolerated
            (exception not raised). False if these models should raise an exception.
            (Default: False).
    Returns:
        str: The default accept type to use for the model.

    Raises:
        ValueError: If the combination of arguments specified is not supported.
    """
    if not jumpstart_utils.is_jumpstart_model_input(model_id, model_version):
        raise ValueError(
            "Must specify JumpStart `model_id` and `model_version` when retrieving accept types."
        )

    return artifacts._retrieve_default_accept_type(
        model_id,
        model_version,
        region,
        tolerate_vulnerable_model,
        tolerate_deprecated_model,
    )
