function pcdOutput() {
    //发送topic
    // 只需要filename.pcd即可，保存在/home/cwh/real_data/中
    let pcdfilepath = $("#ndt_mapping_output").val();
    console.log('pcdOutput index.html:', pcdfilepath)
    //发送话题，保存这个值

    // Publishing a Topic
    var pcdOutputPub = new ROSLIB.Topic({
        ros: ros,
        name: 'cwh_output',
        messageType: 'std_msgs/String'
    });

    var filepathMsg = new ROSLIB.Message({
        data: pcdfilepath
    });

    pcdOutputPub.publish(filepathMsg);
}