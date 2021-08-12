#!/bin/env python3
#
# OCMon - top like monitor for Openshift/Kubernetes
#
import openshift as oc

print('OpenShift client version: {}'.format(oc.get_client_version()))
print('OpenShift server version: {}'.format(oc.get_server_version()))