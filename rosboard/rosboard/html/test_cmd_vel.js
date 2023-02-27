function cmd_vel() {
    console.log('send cmd_vel')
    // Publishing a Topic
    var cmdVel = new ROSLIB.Topic({
        ros: ros,
        name: 'turtle1/cmd_vel',
        messageType: 'geometry_msgs/Twist'
    });//创建一个topic,它的名字是'/cmd_vel',,消息类型是'geometry_msgs/Twist' 


    // console.log('msg', cmdVel)
    // cmdVel.subscribe((msg) => {
    //   console.log('msg', msg)
    // });

    var twist = new ROSLIB.Message({
        linear: {
            x: 1.0,
            y: 0.0,
            z: 0.0
        },
        angular: {
            x: 0.0,
            y: 0.0,
            z: 1.0
        }
    });//创建一个message

    setInterval(() => {
        cmdVel.publish(twist);//发布twist消息
    }, 1000 / 15);
}