import { useEffect } from "react";
import { useRouter } from "next/router";

export default function CreateNote(){
    const router = useRouter();

    useEffect(() => {
        if(router.isReady){
            fetch('http://localhost:8000/api/notes/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
            }).then((res) => {
                return res.json();
            }).then((data) => {
                router.push(`/${data.uuid}`)
            })
        }
    })

    return (
        <div>
            Creating note...
            This should eventually be a loader
        </div>
    )
}