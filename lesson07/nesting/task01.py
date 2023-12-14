devices = {
    'r1': {
        'location': 'Bukhara',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': 'Samarkand',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': 'Tashkent',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
dvc = []
for i in devices:
    dvc.append(i)
delim = '/'
dvc_str = delim.join(dvc)

device = input(f'Введите название устройства [{dvc_str}]: ')

if device in devices:
    location = devices.get(device).get('location')
    print(f'Расположен          {location}')
    vendor = devices.get(device).get('vendor')
    print(f'Вендор              {vendor}')
    model = devices.get(device).get('model')
    print(f'Модель              {model}')
    ios = devices.get(device).get('ios')
    print(f'Система (ios)       {ios}')
    ip = devices.get(device).get('ip')
    print(f'IP адрес            {ip}')
    vlans = devices.get(device).get('vlans')
    print(f'Выделенные сети     {vlans}')
    routing = devices.get(device).get('routing')
    print(f'Маршрутизатор       {routing}')
else:
    print('Устройство не существует')

