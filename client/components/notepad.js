import React, { useState, useEffect, useContext } from 'react'
import Footer from '../components/footer'
import { socket, joinNote, writeNote, SocketContext } from '../contexts/useSocket';


export default function Notepad(props) { 
    const [content, setContent] = useState(props.note.content);
    const [note, setNote] = useState(props.note); // redundant unless note object becomes more complex
    const [joined, setJoined ] = useState(false);
    const socket = useContext(SocketContext);
    const [message, setMessage] = useState(socket);
    
    useEffect(() => {
        // TODO: connect to websocket
        if(!joined){
            joinNote(note.uuid);
            setJoined(true);
        }
        // only refresh component if the message is relevant to this component
        if(socket !== message){
            console.log('message', message)
            if(message.message === 'new-join'){
                setNote(message.data)
                setMessage(socket)
                setContent(message.data.content)
            }
        }
    }, [message, content])

    const handleWrite = (e) => {
        setContent(e.target.value)
    }

    return (
        <>
            <div id="content-body">
                <textarea 
                    name="content"
                    id="content"
                    value={content}
                    onChange={handleWrite}
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
