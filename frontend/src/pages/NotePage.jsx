import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { ReactComponent as ArrowLeft } from "../assets/arrow-left.svg"

const NotePage = ( ) => {

    //let noteId = match.params.id // ".id" porque es lo que le pasamos en el Route "/:id"
    const  {noteId}  = useParams()
    const navigate = useNavigate()
    
    let [note, setNote] = useState(null)

    useEffect(() => {
        let getNote = async () => {
            if (noteId === 'new') return
    
            let response = await fetch(`/api/notes/${noteId}/`) // En DJANGO era "/api/notes/" en plural, y no "note"
            let data = await response.json()
            setNote(data)
        }

        getNote()
    }, [noteId])



    let createNote = async () => {
        fetch(`/api/notes/create`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }


    let updateNote = async () => {
        fetch(`/api/notes/${noteId}/update`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }


    let deleteNote = async () => {
        fetch(`/api/notes/${noteId}/delete`, {
            method: "DELETE",
            headers: {
                'Content-Type': 'application/json'
            }
        })
        navigate('/')
    }




    let handleSubmit = () => {
        if (noteId !== 'new' && note.body === '') {
            deleteNote()
        } else if (noteId !== 'new') {
            updateNote()
        } else if (noteId === 'new' && note.body !== null) {
            createNote()
        }
        navigate('/')
    }

    let handleChange = (value) => {
        setNote((prevState) => {return {...prevState, body:value}})
    }
    

    // Cuando se haga click sobre la nota, se va a poder editar, porque en el listItem pusimos Link, o sea, 
    // lo que hace en realidad es redirigir a la nota, pero aca la transforma en un textares, entonces se puede editar
    return (
        <div className='note'>
            <div className="note-header">
                <h3>
                    <ArrowLeft onClick={handleSubmit} />
                </h3>
                {noteId !== 'new' ? (
                    <button onClick={deleteNote}>Delete</button>
                ) : (
                    <button onClick={handleSubmit}>Done</button>
                )
                }
            </div>
            <textarea onChange={(e)=> {handleChange(e.target.value)}} value={note?.body}></textarea>
        </div>
    )
}

export default NotePage