import {test} from 'node:test';
import assert from 'node:assert/strict';
import {handler} from '../netlify/functions/stylist.mjs';
import vercelStylist from '../api/stylist.mjs';

const response=()=>({headers:{},statusCode:0,body:null,setHeader(k,v){this.headers[k]=v;},status(code){this.statusCode=code;return this;},json(body){this.body=body;return this;}});

test('Netlify stylist rejects invalid methods, oversized and malformed input',async()=>{
 const method=await handler({httpMethod:'GET',headers:{},body:''});
 assert.equal(method.statusCode,405);
 const large=await handler({httpMethod:'POST',headers:{},body:' '.repeat(4097)});
 assert.equal(large.statusCode,413);
 const malformed=await handler({httpMethod:'POST',headers:{},body:'{' });
 assert.equal(malformed.statusCode,400);
});

test('Netlify stylist rejects cross-origin requests and falls back without AI credentials',async()=>{
 const denied=await handler({httpMethod:'POST',headers:{origin:'https://other.example',host:'velmora.example'},body:JSON.stringify({message:'black tie'})});
 assert.equal(denied.statusCode,403);
 const response=await handler({httpMethod:'POST',headers:{host:'velmora.example'},body:JSON.stringify({message:'black tie'})});
 assert.equal(response.statusCode,503);
 assert.match(JSON.parse(response.body).error,/not configured/i);
});

test('Vercel stylist uses the same request boundaries and no-key fallback',async()=>{
 let res=response();await vercelStylist({method:'GET',headers:{}},res);assert.equal(res.statusCode,405);
 res=response();await vercelStylist({method:'POST',headers:{},body:' '.repeat(4097)},res);assert.equal(res.statusCode,413);
 res=response();await vercelStylist({method:'POST',headers:{},body:'{'},res);assert.equal(res.statusCode,400);
 res=response();await vercelStylist({method:'POST',headers:{origin:'https://other.example',host:'velmora.example'},body:{message:'black tie'}},res);assert.equal(res.statusCode,403);
 res=response();await vercelStylist({method:'POST',headers:{host:'velmora.example'},body:{message:'black tie'}},res);assert.equal(res.statusCode,503);assert.match(res.body.error,/not configured/i);
});
