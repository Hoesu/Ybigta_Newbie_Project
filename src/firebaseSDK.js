// Import the functions you need from the SDKs you need
import { getAuth } from "firebase/auth";
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";



const firebaseConfig = {
  //프로젝트 키 숨김
};

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);
const firebaseAnalytics = getAnalytics(firebaseApp);


export default 
{ firebaseApp, firebaseAnalytics };

export const authService = getAuth(firebaseApp);
export const dbService = getFirestore(firebaseApp);
export const storageService = getStorage(firebaseApp);