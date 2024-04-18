import { Link } from "react-router-dom"
import { useParams } from "react-router-dom"
import './index.css'


export default function List(props){


    const deleteuser=(index)=>{
        alert(index)
        let updateUser = props.users.filter((user,i)=>i!=index )
          props.setUsers(updateUser)
        
    }
    return (
        <>
        <h1>List Page</h1>
        <table border={1}>
            <thead>
                <tr>
                   <th>Name</th>
                   <th>Email</th>
                   <th>View</th>
                   <th>Edit</th>
                   <th>Delete</th>
                </tr>
            </thead>
            <tbody>
                {
                    props.users.map((user,i)=>{
                       
                        return(
                            <tr key={i}>
                               <td>{user.name}</td>
                               <td>{user.email}</td>
                               <td><Link to={`/user/view/${user.name}`}>View</Link></td>
                               <td><Link to={`/user/edit/${user.name}`}>Edit</Link></td>
                               <td><button type="button" onClick={()=>deleteuser(i)}>Delete</button></td>
                            </tr>



                        )
                    })
                }
            </tbody>
        </table>
        <td><Link className="link"   to={"/user/create"}>Go back</Link></td>
        </>
    )
}