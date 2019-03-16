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
    function handle_response(data) {
        // append the bot repsonse to the div
        console.log(data);
        $('.chat-container').append(`
                <div class="chat-message col-md-5 bot-message">
                    ${data.fulfillmentText}
                </div>
          `)
        // remove the loading indicator
        $("#loading").remove();
    }
}
  
  //var chat = {"Hi":"Hi","Hi2":"Hi2","Hi3":"Hi3"}