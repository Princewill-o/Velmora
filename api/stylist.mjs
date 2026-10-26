import {parseIntent} from '../ai.mjs';

export default async function stylist(req,res){
 res.setHeader('Content-Type','application/json; charset=utf-8');
 res.setHeader('Cache-Control','no-store');
 if(req.method!=='POST')return res.status(405).json({error:'POST required.'});
 let input=req.body;
 if(typeof input==='string'){
  if(Buffer.byteLength(input,'utf8')>4096)return res.status(413).json({error:'Request is too large.'});
  try{input=JSON.parse(input);}catch{return res.status(400).json({error:'A JSON request is required.'});}
 }else if(input&&typeof input==='object'){
  if(Buffer.byteLength(JSON.stringify(input),'utf8')>4096)return res.status(413).json({error:'Request is too large.'});
 }else return res.status(400).json({error:'A JSON request is required.'});
 const origin=req.headers?.origin,host=req.headers?.host;
 if(origin&&host){try{if(new URL(origin).host!==host)return res.status(403).json({error:'Same-origin requests only.'});}catch{return res.status(403).json({error:'Invalid request origin.'});}}
 const result=await parseIntent(input?.message);
 return res.status(result.status).json(result.body);
}
