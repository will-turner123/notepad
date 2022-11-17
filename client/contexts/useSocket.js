import { createContext, useState, useEffect } from "react";
import { connect, io } from "socket.io-client";
// will update every time the socket emits a message

export const socket = io("ws://127.0.0.1:8000/");

export const SocketContext = createContext();

export const SocketProvider = ({ children }) => {
    const [value, setValue] = useState({});

    useEffect(() => {
        initSockets({ setValue });
    }, [initSockets]);

    return (
        <SocketContext.Provider value={ value } >
            {children}
        </SocketContext.Provider>
    );
};


export const initSockets = ({ setValue }) => {
    socketEvents({ setValue });
};


// for tomorrow: https://alexboots.medium.com/using-react-context-with-socket-io-3b7205c86a6d

// will update every time the socket emits a message TODO: move to separate file
// IDEA: Given that the socket is a global variable, we can just import it into any component that needs it
// ^ that was copilot
// the setValue is passed. It could be used to set anything
// Check out Recoil. Could have a global store type of thing
export const socketEvents = ({ setValue }) => {
    socket.on('connected', (message) => {
        // setValue(state => { return { ...state, message } });
        console.log('message', message)
        setValue(message);
    });

    socket.on('new-join', (message) => {
        setValue(state => { return { 'message': 'new-join', 'data': message } });
    })
}

export const test = () => {
    socket.emit('test');
}

// emit messages to the server
export const joinNote = (noteId) => {
    socket.emit('join-note', noteId);
}



// import { createContext, useEffect, useState } from 'react';
// import { Server } from 'socket.io';

// const SocketContext = createContext();

// const SocketProvider = ({ children }) => {
//     const [socket, setSocket] = useState(null);
    
//     useEffect(() => {
//         if(typeof window !== 'undefined'){
//             if(!socket){
//                 console.log('here')
//                 const io = new Server("ws://localhost:8000/");
//                 setSocket(io);
//             }
//         }
//     }, [socket]);

//     return (
//         <SocketContext.Provider value={socket}>
//             {children}
//         </SocketContext.Provider>
//     )
// }

// const useSocket = () => {
//     const socket = useContext(SocketContext);
//     return socket;
// }

// export { SocketProvider, useSocket }