import monitorcontrol

print(monitorcontrol.get_monitors())
monitor = monitorcontrol.get_monitors()[0]
print(monitor)
with monitor:
	# print(monitor.get_vcp_capabilities())
	print(monitor.get_input_source())
	monitor.set_input_source('HDMI2')
	# print(monitor.get_input_source())
	# monitor.set_input_source('HDMI1')
	# print(monitor.get_input_source())

