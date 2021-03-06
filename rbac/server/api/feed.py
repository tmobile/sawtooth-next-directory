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
"""Socket feed enabling real-time notifications of proposals."""
import json

from rbac.common.logs import get_default_logger
from rbac.providers.common.common import escape_user_input
from rbac.server.api.proposals import compile_proposal_resource
from rbac.server.api import utils
from rbac.server.db import proposals_query
from rbac.server.db.db_utils import create_connection

LOGGER = get_default_logger(__name__)


async def handle_feed_socket(sio, data):
    """Socket feed enabling real-time notifications"""
    required_fields = ["next_id"]
    recv = json.loads(data)
    utils.validate_fields(required_fields, recv)
    await proposal_feed(sio, recv)


async def proposal_feed(sio, recv):
    """Send open proposal updates to a given user"""
    conn = await create_connection()
    subscription = await proposals_query.subscribe_to_proposals(conn)
    while await subscription.fetch_next():
        proposal = await subscription.next()
        proposal_resource = await compile_proposal_resource(
            conn, proposal.get("new_val")
        )

        conn.close()

        next_id = escape_user_input(recv.get("next_id"))
        if (
            proposal_resource["status"] == "OPEN"
            and next_id in proposal_resource["approvers"]
        ):
            await sio.emit("feed", json.dumps({"open_proposal": proposal_resource}))
        if next_id == proposal_resource["opener"]:
            await sio.emit("feed", json.dumps({"user_proposal": proposal_resource}))
