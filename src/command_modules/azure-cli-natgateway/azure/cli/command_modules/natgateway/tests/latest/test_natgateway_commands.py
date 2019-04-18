# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import re

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer


class NatGatewayScenarioTests(ScenarioTest):

    @ResourceGroupPreparer(location='eastus2')
    def test_create_natgateway(self, resource_group, resource_group_location):

        self.kwargs.update({
            'resource_group': resource_group,
            'name': "ng1",
            'idle_timeout': 4,
            'sku' : "Standard",
            'publicipaddress' : "None",
            'publicipprefix' : "None",
            'location' : resource_group_location,
            'resource_type': 'Microsoft.Network/NatGateways'
        })

        # create
        create_cmd = 'az network nat-gateway create --resource-group {resource_group} --nat-gateway-name {name} --location {location} --public-ip-address  {publicipaddress} --public-ip-address {publicipprefix} --idle-timeout {idle_timeout}'

        self.cmd(create_cmd, checks=[
            self.check('resourceGroup', '{resource_group}'),
            self.check('idleTimeoutInMinutes', '{idle_timeout}'),
            self.check('sku.name', 'Standard'),
            self.check('publicIpAddresses', '{publicipaddress}'),
            self.check('publicIpPrefixes', '{publicipprefix}'),
            self.check('location', '{location}')
        ])

        # delete
        delete_cmd = 'az network nat-gateway delete --resource-group {resource_group} --nat-gateway-name {name}'

        self.cmd(delete_cmd);