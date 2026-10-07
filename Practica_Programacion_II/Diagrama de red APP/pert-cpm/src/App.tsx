import {useMemo,useRef,useState} from 'react'
import ReactFlow,{Background,Handle,MarkerType,Position,ReactFlowProvider,type Node,type Edge as RFEdge} from 'reactflow'
import {toPng} from 'html-to-image'
import {jsPDF} from 'jspdf'
import {Act,Res,cpm,crash,parse,slope} from './cpm'

const SAMPLE=`T1 | 2 | 1 | 100 | 150 | Inicio
T2 | 3 | 2 | 200 | 300 | T1
T3 | 24 | 18 | 1000 | 1800 | T2
T4 | 10 | 8 | 500 | 700 | T3
T5 | 13 | 10 | 300 | 420 | T1, T3`

const RED='#b91c1c',BLK='#1f2937'
const Cell=({v,c}:{v:number;c?:string})=><div className={`flex-1 text-center text-[12px] font-semibold py-0.5 border-slate-700 ${c||''}`}>{v}</div>

function ActNode({data}:{data:any}){
  const k=data.crit,bd=k?'border-red-800':'border-slate-600',bg=k?'bg-red-200':'bg-slate-200'
  const ln=`border-b ${k?'border-red-800':'border-slate-600'}`
  return <div className={`w-[130px] border-2 ${bd} ${bg} rounded-sm text-slate-900`}>
    <Handle type="target" position={Position.Left} style={{opacity:0}}/>
    <div className={`flex divide-x ${k?'divide-red-800':'divide-slate-600'} ${ln} bg-white/60`}><Cell v={data.ES}/><Cell v={data.cur}/><Cell v={data.EF}/></div>
    <div className={`text-center text-sm font-bold py-1.5 ${ln}`}>{data.id}</div>
    <div className={`flex divide-x ${k?'divide-red-800':'divide-slate-600'} bg-white/60`}><Cell v={data.LS}/><Cell v={data.H}/><Cell v={data.LF}/></div>
    <Handle type="source" position={Position.Right} style={{opacity:0}}/>
  </div>
}
const TermNode=({data}:{data:any})=><div className="px-4 py-2 rounded-full border-2 border-red-800 bg-red-100 text-sm font-bold">{data.id}
  <Handle type="target" position={Position.Left} style={{opacity:0}}/><Handle type="source" position={Position.Right} style={{opacity:0}}/></div>
const nodeTypes={act:ActNode,term:TermNode}

function Diagram({title,res}:{title:string;res:Res}){
  const {nodes,edges}=useMemo(()=>{
    const lvl:Record<string,number>={Inicio:0},cnt:Record<number,number>={}
    const preds=(id:string)=>res.rows.find(r=>r.id===id)!.pred
    res.order.forEach(id=>{const p=preds(id);lvl[id]=p.length?Math.max(...p.map(x=>lvl[x]))+1:1})
    const maxL=Math.max(...Object.values(lvl));lvl.Fin=maxL+1
    const place=(id:string,type:string,data:any):Node=>{const l=lvl[id];const i=cnt[l]=(cnt[l]??-1)+1
      return{id,type,data,position:{x:l*200,y:i*120+(type==='term'?30:0)},draggable:true}}
    const nodes=[place('Inicio','term',{id:'Inicio'}),...res.rows.map(r=>place(r.id,'act',r)),place('Fin','term',{id:'Fin'})]
    const edges:RFEdge[]=res.edges.map(e=>({id:e.s+'-'+e.t,source:e.s,target:e.t,type:'smoothstep',
      style:{stroke:e.crit?RED:BLK,strokeWidth:e.crit?2.2:1.4},markerEnd:{type:MarkerType.ArrowClosed,color:e.crit?RED:BLK}}))
    return{nodes,edges}},[res])
  return <div className="bg-white border border-slate-300 rounded-lg shadow-sm overflow-hidden">
    <div className="px-4 py-2 bg-slate-800 text-white flex justify-between text-sm">
      <b>{title}</b><span>Duración: <b>{res.dur}</b> · Coste: <b>{res.cost.toLocaleString()}</b></span></div>
    <div className="px-4 py-1.5 text-sm border-b bg-red-50 text-red-900">
      <b>Ruta crítica{res.paths.length>1?'s':''}:</b> {res.paths.map(p=>p.join(' → ')).join('  |  ')}</div>
    <div style={{height:380}}>
      <ReactFlowProvider><ReactFlow nodes={nodes} edges={edges} nodeTypes={nodeTypes} fitView fitViewOptions={{padding:0.15}}
        proOptions={{hideAttribution:true}} nodesConnectable={false} minZoom={0.3}><Background gap={20} color="#e5e7eb"/></ReactFlow></ReactFlowProvider></div>
    <div className="px-4 py-1.5 text-[11px] text-slate-600 border-t flex gap-4 flex-wrap">
      <span>Fila sup.: <b>ES | D | EF</b> (Inicio Temprano, Duración, Fin Temprano)</span>
      <span>Fila inf.: <b>LS | H | LF</b> (Inicio Tardío, Holgura, Fin Tardío)</span>
      <span className="text-red-700">■ Crítica</span><span>■ No crítica</span></div>
  </div>
}

export default function App(){
  const [text,setText]=useState(SAMPLE),[target,setTarget]=useState(''),[over,setOver]=useState<Record<string,number>>({}),[log,setLog]=useState<string[]>([])
  const area=useRef<HTMLDivElement>(null)
  const {acts,orig,acc,err}=useMemo(()=>{
    try{const acts=parse(text)
      const cur=Object.fromEntries(acts.map(a=>[a.id,Math.min(a.d,Math.max(a.dmin,over[a.id]??a.d))]))
      return{acts,orig:cpm(acts,{}),acc:cpm(acts,cur),err:''}}
    catch(e:any){return{acts:[] as Act[],orig:null,acc:null,err:e.message as string}}},[text,over])
  const setDur=(a:Act,v:number)=>setOver(o=>({...o,[a.id]:Math.min(a.d,Math.max(a.dmin,v||a.d))}))
  const auto=()=>{const t=Number(target);if(!t||!orig)return
    const r=crash(acts,t);setOver(r.cur);setLog(r.log)}
  const img=()=>toPng(area.current!,{pixelRatio:2,backgroundColor:'#ffffff'})
  const png=async()=>{const a=document.createElement('a');a.href=await img();a.download='pert-cpm.png';a.click()}
  const pdf=async()=>{const d=await img(),el=area.current!
    const p=new jsPDF({orientation:'landscape',unit:'px',format:[el.offsetWidth+40,el.offsetHeight+40]})
    p.addImage(d,'PNG',20,20,el.offsetWidth,el.offsetHeight);p.save('pert-cpm.pdf')}
  const btn='px-3 py-1.5 rounded text-sm font-medium border'
  return <div className="min-h-screen">
    <header className="bg-slate-900 text-white px-6 py-3 flex items-center justify-between">
      <h1 className="font-semibold">Diagrama PERT/CPM · Gestión de Proyectos</h1>
      <div className="flex gap-2"><button className={`${btn} bg-white text-slate-900`} onClick={png} disabled={!!err}>Exportar PNG</button>
      <button className={`${btn} bg-red-600 border-red-600`} onClick={pdf} disabled={!!err}>Exportar PDF</button></div></header>
    <div className="grid grid-cols-12 gap-4 p-4">
      <aside className="col-span-12 lg:col-span-4 space-y-4">
        <section className="bg-white rounded-lg border p-3 shadow-sm">
          <h2 className="font-semibold text-sm mb-1">Actividades</h2>
          <p className="text-[11px] text-slate-500 mb-1">ID | Dur. normal | Dur. acelerada mín. | Coste normal | Coste acelerado | Predecesoras</p>
          <textarea value={text} onChange={e=>{setText(e.target.value);setOver({});setLog([])}} rows={9} spellCheck={false}
            className="w-full font-mono text-xs border rounded p-2 focus:outline-none focus:ring-2 focus:ring-red-300"/>
          {err&&<p className="text-red-700 text-xs mt-1">⚠ {err}</p>}
        </section>
        {!err&&<section className="bg-white rounded-lg border p-3 shadow-sm">
          <h2 className="font-semibold text-sm mb-2">Simulador de aceleración</h2>
          <div className="flex gap-2 mb-2"><input type="number" placeholder={`Duración objetivo (< ${orig!.dur})`} value={target} onChange={e=>setTarget(e.target.value)} className="flex-1 border rounded px-2 py-1 text-sm"/>
            <button onClick={auto} className={`${btn} bg-slate-800 text-white`}>Auto</button>
            <button onClick={()=>{setOver({});setLog([])}} className={`${btn} bg-white`}>Reiniciar</button></div>
          <table className="w-full text-xs"><thead><tr className="text-left text-slate-500 border-b"><th>Act.</th><th>Dn</th><th>Dmín</th><th>Pend. coste</th><th>Dur. manual</th></tr></thead>
            <tbody>{acts.map(a=><tr key={a.id} className="border-b">
              <td className={`font-semibold ${acc!.rows.find(r=>r.id===a.id)!.crit?'text-red-700':''}`}>{a.id}</td><td>{a.d}</td><td>{a.dmin}</td>
              <td>{a.d>a.dmin?slope(a).toFixed(1):'—'}</td>
              <td><input type="number" min={a.dmin} max={a.d} value={over[a.id]??a.d} disabled={a.d===a.dmin} onChange={e=>setDur(a,+e.target.value)} className="w-14 border rounded px-1"/></td></tr>)}</tbody></table>
          {log.length>0&&<ol className="mt-2 text-[11px] text-slate-600 list-decimal pl-4 max-h-40 overflow-auto">{log.map((l,i)=><li key={i}>{l}</li>)}</ol>}
        </section>}
        {!err&&<section className="bg-white rounded-lg border p-3 shadow-sm text-sm">
          <h2 className="font-semibold mb-1">Comparación</h2>
          <div className="grid grid-cols-3 gap-1 text-xs"><b/><b>Original</b><b>Acelerado</b>
            <span>Duración</span><span>{orig!.dur}</span><span>{acc!.dur}</span>
            <span>Coste</span><span>{orig!.cost.toLocaleString()}</span><span>{acc!.cost.toLocaleString()}</span>
            <span>Δ</span><span/><span>{(acc!.cost-orig!.cost>=0?'+':'')+(acc!.cost-orig!.cost).toLocaleString()} / {acc!.dur-orig!.dur} u</span></div></section>}
      </aside>
      <main className="col-span-12 lg:col-span-8">
        {!err&&<div ref={area} className="space-y-4 bg-white p-4">
          <Diagram title="ESCENARIO ORIGINAL" res={orig!}/>
          <Diagram title="ESCENARIO ACELERADO" res={acc!}/></div>}
      </main>
    </div></div>
}
