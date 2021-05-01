(async () => {
  const useFrameRate = 30;
  const stream = await navigator.mediaDevices.getUserMedia ({video: true});
  const capture = new ImageCapture (stream.getVideoTracks ()[0]);
  const socket = new WebSocket ('ws://localhost:3333');
  const options = {imageWidth: 640, imageHeight: 480};
  socket.addEventListener ('open', () => {
    const send = () =>
      capture
        .takePhoto (options)
        .then (blob => socket.send (blob))
        .catch (() => {});
    const sendloop = setInterval (send, 250);
  });

  socket.onmessage = e => {
    socket.binaryType = 'arraybuffer';
    console.log (e.data);

    var iData = new ImageData (new Uint8ClampedArray (e.data), 360, 270);
    var ctx = canvas.getContext ('2d');
    ctx.putImageData (iData, 0, 0);
    //FUNCIONOU___________________________________________________________
    /*     var arrayBuffer = e.data;
    var bytes = new Uint8Array (arrayBuffer);
    var blob = new Blob ([bytes.buffer]);
    var image = document.getElementById ('image');
    var reader = new FileReader ();
    reader.onload = function (e) {
      image.src = e.target.result;
    };
    reader.readAsDataURL (blob); */
    //console.log (JSON.parse (e.data));
    /*     let reader = new FileReader ();
    reader.readAsDataURL (e.data);
    reader.onload = function () {
      var b64 = reader.result.replace (/^data:.+;base64,/, '');
      var b64img = atob (b64);
      var canvas = document.querySelector ('canvas');
      var ctx = canvas.getContext ('2d');
      var image = new Image ();
      ctx.drawImage (image, 0, 0);
      console.log (image); //-> "Welcome to <b>base64.guru</b>!"
      image.src = 'data:image/png;base64,' + b64img;
    }; */
    /*     var reader2 = new FileReader ();
    reader2.onload = function (e) {
      var img = document.getElementById ('image');
      img.src = e.target.result;
    };
    reader2.readAsDataURL (e.data);
 */
    /*     function drawImage (imgString) {
      var canvas = document.getElementById ('canvas');
      var ctx = canvas.getContext ('2d');
      var image = new Image ();
      image.src = imgString;
      ctx.drawImage (image, 0, 0);
      console.log (window.btoa (imgString));
    }
    drawImage (reader.result); */
  };
  if (navigator.getUserMedia) {
    navigator.getUserMedia (
      {audio: false, video: {width: 360, height: 270}},
      function (stream) {
        var video = document.querySelector ('video');
        video.srcObject = stream;
        video.onloadedmetadata = function (e) {
          video.play ();
        };
      },
      function (err) {
        console.log ('The following error occurred: ' + err.name);
      }
    );
  } else {
    console.log ('getUserMedia not supported');
  }
}) ();
