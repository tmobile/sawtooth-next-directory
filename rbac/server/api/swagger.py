# Copyright 2019 Contributors to Hyperledger Sawtooth
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------
"""Provides the API swagger."""

from sanic import Blueprint
from sanic import response

from rbac.common.logs import get_default_logger

LOGGER = get_default_logger(__name__)

SWAGGER_BP = Blueprint("swagger")


@SWAGGER_BP.get("api/swagger")
async def get_swagger(request):
    """Returns pretty swagger file for our API."""
    if not request:
        LOGGER.debug(str(request))
    return await response.file(
        "/project/hyperledger-rbac/rbac/server/swagger/index.html",
        headers={"Content-Type": "text/html; charset=utf-8"},
    )