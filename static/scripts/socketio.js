document.addEventListener('DOMContentLoaded', () =>{
    var socket = io();
    socket.on('message',data => {
        const p = document.createElement('p');
        const span_user = document.createElement('span')
        const br = document.createElement('br');
        const span_time = document.createElement('span');
        span_time.innerHTML = data.time_stamp
        span_user.innerHTML = data.username
        p.innerHTML = span_user.outerHTML + span_time.outerHTML + br.outerHTML + data.msg + br.outerHTML;
        document.querySelector('#message_window').append(p);
    });

    socket.on('some-event', data =>{
        console.log(data)
    });
    // Отправка сообщения на сервер
    document.querySelector('#send_message').onclick = () => {
        socket.send({'msg': document.querySelector('#user_message').value, 'username': username});
    }
})