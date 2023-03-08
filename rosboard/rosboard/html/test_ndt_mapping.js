function startNdtMapping() {
    // 启动建图，传递参数
    console.log('startNdtMapping')

    var service = new ROSLIB.Service({
        ros: ros,
        name: '/run_roslaunch', // roslaunch服务的名称
        serviceType: 'rosbridge_library/LaunchFile'
    })

    var request = new ROSLIB.ServiceRequest({
        filename: 'ndt_mapping'
    });

    service.callService(request, function (result) {
        console.log('Result for service call on ' + service.name + ': ' + result.success + ': ' + result.message);
    });
}