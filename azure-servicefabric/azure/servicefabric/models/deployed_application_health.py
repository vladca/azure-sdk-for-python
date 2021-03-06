# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .entity_health import EntityHealth


class DeployedApplicationHealth(EntityHealth):
    """Information about the health of an application deployed on a Service
    Fabric node.

    :param aggregated_health_state: The HealthState representing the
     aggregated health state of the entity computed by Health Manager.
     The health evaluation of the entity reflects all events reported on the
     entity and its children (if any).
     The aggregation is done by applying the desired health policy.
     . Possible values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str
    :param health_events: The list of health events reported on the entity.
    :type health_events: list of :class:`HealthEvent
     <azure.servicefabric.models.HealthEvent>`
    :param unhealthy_evaluations: The unhealthy evaluations that show why the
     current aggregated health state was returned by Health Manager.
    :type unhealthy_evaluations: list of :class:`HealthEvaluationWrapper
     <azure.servicefabric.models.HealthEvaluationWrapper>`
    :param name: Name of the application deployed on the node whose health
     information is described by this object.
    :type name: str
    :param node_name: Name of the node where this application is deployed.
    :type node_name: str
    :param deployed_service_package_health_states: Deployed service package
     health states for the current deployed application as found in the
     health store.
    :type deployed_service_package_health_states: list of
     :class:`DeployedServicePackageHealthState
     <azure.servicefabric.models.DeployedServicePackageHealthState>`
    """ 

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'health_events': {'key': 'HealthEvents', 'type': '[HealthEvent]'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
        'name': {'key': 'Name', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'deployed_service_package_health_states': {'key': 'DeployedServicePackageHealthStates', 'type': '[DeployedServicePackageHealthState]'},
    }

    def __init__(self, aggregated_health_state=None, health_events=None, unhealthy_evaluations=None, name=None, node_name=None, deployed_service_package_health_states=None):
        super(DeployedApplicationHealth, self).__init__(aggregated_health_state=aggregated_health_state, health_events=health_events, unhealthy_evaluations=unhealthy_evaluations)
        self.name = name
        self.node_name = node_name
        self.deployed_service_package_health_states = deployed_service_package_health_states
