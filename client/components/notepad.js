import React, { useState, useEffect, useContext } from 'react'
import Footer from '../components/footer'
import { socket, write } from '../contexts/useSocket';

// TODO: if we go with this drunken design pattern, we will have to account for an invalid uuid
export default function Notepad({ uuid }) { 
    // const [content, setContent] = useState(props.note.content);
    // const [note, setNote] = useState(props.note); // redundant unless note object becomes more complex
    // const [onlineUsers, setOnlineUsers] = useState([])
    // const [joined, setJoined ] = useState(false);

    const [loading, setLoading] = useState(true);
    const [content, setContent] = useState(""); // perhaps null would be more apt?
    const [onlineUsers, setonlineUsers] = useState(0); // This should eventually be an array

    useEffect(() => {
        console.log('emitting a join', uuid)
        socket.emit('join-note', uuid)
        // loaded after join-note and any time a new user hops in the note
        socket.on('new-join', (data) => {
            console.log('new')
            setonlineUsers(data.online_users);
            setLoading(false);
            
            if(!content){
                setContent(data.content);
            }
        })

        socket.on('note-updated', (data) => {
            console.log('note updated w/', data)
            setContent(data.content);
        })
    

    })



    // const socket = useContext(SocketContext);
    // const [message, setMessage] = useState(socket);
    
    // useEffect(() => {
    //     // TODO: connect to websocket
    //     if(!joined){
    //         joinNote(note.uuid);
    //         setJoined(true);
    //     }
    //     // only refresh component if the message is relevant to this component
    //     if(socket !== message){
    //         console.log('message', message)
    //         if(message.message === 'new-join'){
    //             setNote(message.data)
    //             setMessage(socket)
    //             setContent(message.data.content)
    //         }
    //     }
    // }, [message, content])


    const handleWrite = (e) => {
        // some sort of delay might be wise on this for the sake of performance? avoid constant re-renders?
        setContent(e.target.value)
        console.log('emitting content', content)
        socket.emit('write-note', content)
    }

    return (
        <>
        {loading}
            <div id="content-body">
                <p>debug user count { onlineUsers }</p>
                <textarea 
                    name="content"
                    id="content"
                    value={content}
                    onChange={handleWrite}
                    disabled={loading}
                    sx={{
                        width: '100%',
                        height: '100%',
                    }}
                />
            </div>
            <Footer/>
        </>
    )
}
