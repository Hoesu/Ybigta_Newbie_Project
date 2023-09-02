import Mainpg from "./mainpg";
import Tabpg from "./tabpg";
import { doc, getDoc, collection, getDocs } from "firebase/firestore";
import { dbService, storageService } from "../firebaseSDK";
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";




const Test = () => {
  // useEffect(async () => {
  //   // db 뒤에 "techInfo"는 정보를 가져올 컬렉션 이름이다.
  //     const query = await getDocs(collection(dbService, "all_game_comments")); 
  //     query.forEach((doc) => {
  //       console.log(doc.id, doc.data())
  //     });
  //   }, [])


  // const fetchGameData = async () => {
  //   const querySnapshot = await getDocs(collection(dbService, "all_game_comments"));
  //   querySnapshot.forEach((doc) => {
  //     console.log(doc.id, doc.data());
  //   });
  // };

  // useEffect(() => {
  //   fetchGameData();
  // }, []);

  

  
  const [gameData, setGameData] = useState([]);

  const fetchGameData = async () => {
    const querySnapshot = await getDocs(collection(dbService, "all_game_comments"));

    const games = querySnapshot.docs.map((doc) => ({
      id: doc.id,
      ...doc.data(),
    }));

    setGameData(games);
  };

  useEffect(() => {
    fetchGameData();
  }, []);



  // ------------------------------------------------------



  const [documentData, setDocumentData] = useState(null);

  const fetchDocumentData = async () => {
    try {
      const docRef = doc(dbService, "all_game_comments", "87b2bPNwgEYr3tSnK8gp");
      const docSnapshot = await getDoc(docRef);

      if (docSnapshot.exists()) {
        setDocumentData(docSnapshot.data());
      } else {
        console.log("No such document!");
      }
    } catch (error) {
      console.error("Error fetching document:", error);
    }
  };

  useEffect(() => {
    fetchDocumentData();
  }, []);

  
  return (
    <div className="App">
    
     
     <h2
     style={{
      display: "flex",
      justifyContent: "center",
      marginTop: "25px",
      marginBottom:"25px"
     }}>
      게임 게시판 상위 30개 댓글 
      </h2>

      <ul>
        {gameData.map((game) => (
          <li key={game.id}>
            {game.id} -  {game.score}
          </li>
        ))}
      </ul>

      {/* {documentData && (
        <div>
          <h3>Document Data for 87b2bPNwgEYr3tSnK:</h3>
          <pre>{JSON.stringify(documentData, null, 2)}</pre>
        </div>
      )} */}

<ul>
      {documentData && documentData.maplestory && Object.keys(documentData.maplestory).map((key) => (
        <li key={key}>
          {key}: {documentData.maplestory[key]}
        </li>
      ))}
    </ul>

     <div
     style={{marginBottom: '100px'}}
     >
      <Tabpg />
      </div>


     


      

    </div>
  );
}

export default Test;

// item.id = 문서 id -> 게시판 명