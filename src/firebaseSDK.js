// Import the functions you need from the SDKs you need
import { getAuth } from "firebase/auth";
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";



const firebaseConfig = {
  apiKey: "AIzaSyD6u4WTt7c526z31-5n-zSKxOAXtjK1bFE",
  authDomain: "ybigta-badwords-filter-project.firebaseapp.com",
  projectId: "ybigta-badwords-filter-project",
  storageBucket: "ybigta-badwords-filter-project.appspot.com",
  messagingSenderId: "438814346268",
  appId: "1:438814346268:web:30c48a2c2757914a2d63d9",
  measurementId: "G-TMPTBZE797"
};

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);
const firebaseAnalytics = getAnalytics(firebaseApp);


// const file = lol_comments.csv
// const storageRef = storage.ref();
// const csvFileRef = storageRef.child('path/to/csv/file.csv');
// csvFileRef.put(file)
//   .then(snapshot => {
//     // Get the download URL of the uploaded file
//     return snapshot.ref.getDownloadURL()
//   })
//   .then(url => {
//     // 사용하려는 ReactJS 앱에서 다운로드 URL을 사용
//     // 예를 들어, CSV 파일을 읽고 처리하는 코드 작성
//   })
//   .catch(error => {
//     console.error(error)
//   });


export default 
{ firebaseApp, firebaseAnalytics };

export const authService = getAuth(firebaseApp);
export const dbService = getFirestore(firebaseApp);
export const storageService = getStorage(firebaseApp);