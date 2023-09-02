import Mainpg from "./mainpg";
import Tabpg from "./tabpg";
import { collection, getDocs } from "firebase/firestore"; 
import { dbService, storageService } from "../firebaseSDK";
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Test from "./test";
import { FirebaseApp } from "firebase/app";


// console.log(dbService)
// console.log(storageService)


const App = () => {

  const [predictionResult, setPredictionResult] = useState('');

  useEffect(() => {
    // 클라우드 함수 URL 설정
    const cloudFunctionUrl = 'https://asia-northeast3-ybigta-badwords-filter-project.cloudfunctions.net/function-kobert';

    // HTTP 요청 보내기
    fetch(cloudFunctionUrl)
      .then(response => response.text())
      .then(data => {
        // 응답 데이터 처리
        setPredictionResult(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, []); 

  

  return (
    <div className="App">
      {/* <Router>
        <Routes>
        <Route path ="/test" element={ <Test />} />
        </Routes>
      </Router>

      <a href="/test">test</a> */}
     
     <h2
     style={{
      display: "flex",
      justifyContent: "center",
      marginTop: "25px",
      marginBottom:"25px"
     }}>
      게임 게시판 상위 30개 댓글 
      </h2>

      <Tabpg />

    </div>
  );
}

export default App;

// item.id = 문서 id -> 게시판 명