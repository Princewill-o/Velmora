import {parseIntent} from '../../ai.mjs';

const json=(statusCode,body)=>({statusCode,headers:{'Content-Type':'application/json','Cache-Control':'no-store'},body:JSON.stringify(body)});

export async function handler(event){
 if(event.httpMethod!=='POST')return json(405,{error:'POST required.'});
 const body=event.body||'';
 if(body.length>4096)return json(413,{error:'Request is too large.'});
 const origin=event.headers?.origin,host=event.headers?.host;
 if(origin&&host){try{if(new URL(origin).host!==host)return json(403,{error:'Same-origin requests only.'});}catch{return json(403,{error:'Invalid request origin.'});}}
 let input;try{input=JSON.parse(body);}catch{return json(400,{error:'A JSON request is required.'});}
 const result=await parseIntent(input?.message);
 return json(result.status,result.body);
}
