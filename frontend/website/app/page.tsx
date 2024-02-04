import Image from "next/image";
import Header from './components/header.tsx';
import SearchInput from "./components/SearchInput.tsx";



export default function Home() {
  const handleSearch = (searchValue: string) => {
    // Implement your search logic here (e.g., filter data, make API calls)
    console.log('Search value:', searchValue);
  };
  
  return (
    <main className="flex min-h-screen max-w-screen border w-full flex-col items-center justify-between bg-white">
        <Header/>
      <div className="text-white h-[50rem] w-full flex">
        <div className="basis-3/5 bg-gradient-to-r from-green-400 to-blue-500">
          <div className="text-gray-700 font-bold text-3xl bg-white p-20 m-10 mt-100 mx-200 flex rounded-md items-center w-2/5 h-1/5">
            Ed Tech Forum 
          </div >
          <SearchInput/>
        </div>
        <div className="basis-2/5">
        </div>
        
      </div>
    </main>
  );
}