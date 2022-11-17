import React, { useState, useEffect, useContext } from 'react'
import Footer from '../components/footer'
import { socket } from '../components/socket';


export default function Notepad({ uuid }) { 


    const [loading, setLoading] = useState(true);
    const [content, setContent] = useState(""); // perhaps null would be more apt?
    const [onlineUsers, setonlineUsers] = useState(0); // This should eventually be an array

    useEffect(() => {

        if( socket.connected ) {

            if(loading) {
                socket.emit("join-note", uuid);
            }

            socket.on('new-join', (data) => {
                console.log('successfully joined', data)
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

            socket.on('left-room', (data) => {
                console.log('left room', data)
                setonlineUsers(onlineUsers - 1);
            })

        }
    }, [uuid, socket.connected, loading, onlineUsers])

    const doDebugButton = () => {
        socket.emit('join-note', uuid);
    }

    const handleWrite = (e) => {
        console.log('e.target.value', e.target.value)
        // some sort of delay might be wise on this for the sake of performance? avoid constant re-renders?

        console.log('emitting content', content)
        setContent(e.target.value)
        socket.emit('write-note', {'uuid': uuid, 'content': e.target.value});
    }

    return (
        <>
            <button onClick={doDebugButton}>Debug</button>
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
