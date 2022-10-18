from fastapi import FastAPI
import platform, psutil
import datetime

app = FastAPI()

@app.get("/device/platform")
async def get_platform():
    return {'platform': platform.system(), 'datetime': datetime.datetime.now()}

@app.get("/device/platform/{show_version}")
async def get_platform_release(show_version: bool):
    if(show_version):
        return {'platform': platform.system(), 'release': platform.release(), 'version': platform.version(), 'datetime': datetime.datetime.now()}
    return {'platform': platform.system(), 'release': platform.release(), 'datetime': datetime.datetime.now()}

@app.get("/device/processor")
async def get_processor():
    return {'processor': platform.processor(), 'datetime': datetime.datetime.now()}

@app.get("/device/interfaces/all")
async def get_all_interfaces():
    interfaces = []

    # get all network interfaces (virtual and physical)
    interface_addresses = psutil.net_if_addrs()
    for interface_name in interface_addresses:
        for address in interface_addresses[interface_name]:
            if str(address.family) == 'AddressFamily.AF_INET':  # only IP addresses
                interface = {}
                interface["interface"] = interface_name
                interface["IP address"] = address.address
                interface["netmask"] = address.netmask
                interfaces.append(interface)

    return {'interfaces': interfaces, 'datetime': datetime.datetime.now()}

@app.get("/device/interfaces/{index}")
async def get_interface_by_index(index: int):
    interfaces = []

    # get all network interfaces (virtual and physical)
    interface_addresses = psutil.net_if_addrs()
    for interface_name in interface_addresses:
        for address in interface_addresses[interface_name]:
            if str(address.family) == 'AddressFamily.AF_INET':  # only IP addresses
                interface = {}
                interface["interface"] = interface_name
                interface["IP address"] = address.address
                interface["netmask"] = address.netmask
                interfaces.append(interface)

    if(index < 0 or index > len(interfaces)-1):
        return {"error": "invalid index"}

    return interfaces[index]
