# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def natgateway_client_factory(cli_ctx, **kwargs):
    from azure.cli.core.profiles import ResourceType
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, ResourceType.MGMT_NETWORK, **kwargs)

def create_nat_gateway(cmd, nat_gateway_name, resource_group_name, location, public_ip_address, public_ip_prefix=None, idle_timeout=None):

    client = natgateway_client_factory(cmd.cli_ctx).nat_gateways
    from azure.mgmt.network.models import NatGateway, NatGatewaySku, PublicIPAddress, PublicIPPrefix
    
    nat_gateway = NatGateway(location=location, sku=NatGatewaySku(name='Standard'), PublicIPAddress=public_ip_address, PublicIPPrefix=public_ip_prefix, IdleTimeoutInMinutes=idle_timeout)
    return client.create_or_update(resource_group_name, nat_gateway_name, nat_gateway)

def list_nat_gateways(cmd, resource_group_name=None):
    client = natgateway_client_factory(cmd.cli_ctx).nat_gateways

    return client.list_by_resource_group(resource_group_name)