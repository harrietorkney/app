    $(document).ready(function(){

        var socket = io();
        var counter = 0;
        socket.on('connect', function() {
            console.log("connected!");
        });

        // $('#form').trigger("reset");

        $('#send').click(function() {
            console.log("clicked");
            counter++;
            var userMessage = $("#message").val();
            var userResponse = $("<span class = 'u2 chat' id= 'answer1' type = 'text'>").text(userMessage);
            $("#contact-form").append(userResponse);
            socket.emit('answer'+counter, userMessage);
            $("#message").val("");
        });

        socket.on('answer1', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

        socket.on('answer2', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

        socket.on('answer3', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

        socket.on('answer4', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

        socket.on('answer5', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

        socket.on('answer6', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

         socket.on('answer7', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

          socket.on('answer8', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

          socket.on('answer9', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });


          socket.on('answer10', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

         socket.on('answer11', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

          socket.on('answer12', function(response) {
            for (var i = 0; i < response.length; i++) {
                var serverResponse = $("<span class='u1 chat'></span>").text(response[i]);
                $("#contact-form").append(serverResponse);
            }

        });

//         function updateScroll(){
//     var element = document.getElementByClass(".chat");
//     element.scrollTop = element.scrollHeight;
// }








        

    });

    