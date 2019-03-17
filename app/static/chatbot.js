$('body').ready(function() {
    res({fulfillmentText: 'Hi'})
});
  
function sender() {
    var msg = $('.txt1').val();
    $('.main').append('<div class="txt-div" ><div class="txt msg">'+msg+'</div><div class="time">'+new Date().toLocaleTimeString()+'</div></div>');
    $('.txt1').val('');
    $('.chat').scrollTop = $('.chat').scrollHeight;
    submit_message(msg);
}
  
function res(msg) {
    $('.main').append('<div class="txt-div2" ><div class="txt2 msg">'+msg.fulfillmentText+'</div><div class="time2">'+new Date().toLocaleTimeString()+'</div></div>');
}
 
function submit_message(message) {
    $.post("/send_message", { message: message }, res);
}

var input = document.getElementById("send_msg");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13 && input.value!=="") {
        event.preventDefault();
        document.getElementById('send_btn').click();
    }
});