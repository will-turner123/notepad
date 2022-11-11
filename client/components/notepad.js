var React = require('react');

import { useState, useEffect } from 'react'
import Footer from '../components/footer'

class NotepadComponent extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this)
        this.state = {
            text: "",
            pid: props.pid
        }
        // make this optional, so you can type on a note that hasn't been saved
        if (props.note != undefined) {
            this.state.text = props.note.content;
        }
    }

    handleChange(e) {
        this.setState({text: e.target.value});
    }

    async save_note() {
        let url = 'http://localhost:8000/api/notes/save/'
        if (this.state.pid != undefined) {
            url += this.state.pid
        }
        const res = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        return res.json();
    }

    render() {
        //console.log(this.state.pid)
        // TODO:
        // We succesfully get the ID of the post in the component.
        // Now, we just need to call the save_note function of this class,
        // from the footer component.
        return (
            <>
                <div id="content-body">
                    <textarea 
                        name="content"
                        id="content"
                        value={this.state.text}
                        onChange={this.handleChange}
                        sx={{
                            width: '100%',
                            height: '100%',
                        }}
                    />
                </div>
                <Footer />
            </>
        )
    }
}

export default NotepadComponent