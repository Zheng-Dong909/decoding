if (navigator.mediaDevices.getUserMedia) {
    const constraints = { audio: true };
    navigator.mediaDevices.getUserMedia(constraints).then(stream => {
        console.log("授权成功！");
        const recordBtn = document.getElementById('para');
        const mediaRecorder = new MediaRecorder(stream);
        var chunks = [];
        recordBtn.onclick = function () {
            // console.log(recordBtn)
            // alert("Start Recording");
            if (mediaRecorder.state === "recording") {
                mediaRecorder.stop();
                console.log(chunks)
                mediaRecorder.onstop = e => {
                    var blob = new Blob(chunks, { type: "audio/ogg; codecs=opus" });
                    console.log(blob)
                    var audioURL = window.URL.createObjectURL(blob);
                    const audioSrc = document.querySelector(".audio-player");
                    audioSrc.src = audioURL;
                    var formData = new FormData()
                    formData.append('source', blob)
                    document.getElementById('sub').onclick = function () {
                        $.ajax({
                            url: window.location.href.split("/").at(-1),
                            type: 'POST',
                            data:formData,
                            processData: false,
                            // data: {
                            //     'audio': audioURL,
                            // },
                            error: function (xhr, errmsg, err) {
                                alert(err);
                            }
                        });
                        alert("audio link has been sent.");
                    }
                };

                recordBtn.textContent = "record";
                console.log("Stop Recording");