//前提需要启动turtlesim_node
console.log('test_turtlesim')
function test_turtlesim() {
    var service = new ROSLIB.Service({
        ros: ros,
        name: '/spawn',
        serviceType: 'turtlesim/Spawn'
    })
    
    var request = new ROSLIB.ServiceRequest({
        x : -2.0,
        y : 2.0,
        theta : 0.0,
        name : 'c2'
    })
    
    console.log('1', service)
    console.log('2', request)
    
    service.callService(request, function (result) {
        console.log('====')
        //result not include property of success 
        console.log('Result for service call on ' + service.name + ': ' + result.success)
    });
}