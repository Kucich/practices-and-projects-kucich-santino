export interface Act{id:string;d:number;dmin:number;c:number;cc:number;pred:string[]}
export interface Row extends Act{cur:number;ES:number;EF:number;LS:number;LF:number;H:number;crit:boolean}
export interface Edge{s:string;t:string;crit:boolean}
export interface Res{rows:Row[];dur:number;cost:number;paths:string[][];edges:Edge[];order:string[]}
export const slope=(a:Act)=>a.d>a.dmin?(a.cc-a.c)/(a.d-a.dmin):0

export function parse(text:string):Act[]{
  const acts:Act[]=[]
  text.split('\n').map(l=>l.trim()).filter(Boolean).forEach((l,i)=>{
    const p=l.split(/[|\t;]/).map(s=>s.trim())
    if(p.length<5)throw new Error(`Línea ${i+1}: se esperan 6 columnas (ID | Dn | Dmin | Cn | Cac | Pred)`)
    const n=p.slice(1,5).map(Number)
    if(n.some(isNaN))throw new Error(`Línea ${i+1}: valores numéricos inválidos`)
    if(n[1]>n[0])throw new Error(`Línea ${i+1}: la duración acelerada no puede superar la normal`)
    const pred=(p[5]||'').split(/[,\s]+/).filter(x=>x&&x.toLowerCase()!=='inicio'&&x!=='-')
    acts.push({id:p[0],d:n[0],dmin:n[1],c:n[2],cc:n[3],pred})
  })
  if(!acts.length)throw new Error('Sin actividades')
  return acts
}

// Ordenamiento topológico (Kahn) con detección de ciclos y predecesoras inexistentes
export function topo(acts:Act[]):string[]{
  const ids=new Set(acts.map(a=>a.id))
  if(ids.size!==acts.length)throw new Error('IDs de actividad duplicados')
  const indeg=new Map(acts.map(a=>[a.id,a.pred.length]))
  acts.forEach(a=>a.pred.forEach(p=>{if(!ids.has(p))throw new Error(`${a.id}: predecesora "${p}" no existe`)}))
  const q=acts.filter(a=>!a.pred.length).map(a=>a.id),out:string[]=[]
  while(q.length){const u=q.shift()!;out.push(u)
    acts.forEach(a=>{if(a.pred.includes(u)){const k=indeg.get(a.id)!-1;indeg.set(a.id,k);if(k===0)q.push(a.id)}})}
  if(out.length!==acts.length)throw new Error('Se detectó un ciclo en las dependencias')
  return out
}

export function cpm(acts:Act[],cur:Record<string,number>):Res{
  const order=topo(acts),m=new Map(acts.map(a=>[a.id,a])),R=new Map<string,Row>()
  order.forEach(id=>{const a=m.get(id)!,d=cur[id]??a.d
    const ES=Math.max(0,...a.pred.map(p=>R.get(p)!.EF))
    R.set(id,{...a,cur:d,ES,EF:ES+d,LS:0,LF:0,H:0,crit:false})})
  const dur=Math.max(...[...R.values()].map(r=>r.EF))
  const succ=(id:string)=>acts.filter(a=>a.pred.includes(id)).map(a=>a.id)
  ;[...order].reverse().forEach(id=>{const r=R.get(id)!,s=succ(id)
    r.LF=s.length?Math.min(...s.map(x=>R.get(x)!.LS)):dur
    r.LS=r.LF-r.cur;r.H=r.LS-r.ES;r.crit=r.H===0})
  const edges:Edge[]=[]
  acts.forEach(a=>{const t=R.get(a.id)!
    if(!a.pred.length)edges.push({s:'Inicio',t:a.id,crit:t.crit&&t.ES===0})
    a.pred.forEach(p=>{const s=R.get(p)!;edges.push({s:p,t:a.id,crit:s.crit&&t.crit&&s.EF===t.ES})})
    if(!succ(a.id).length)edges.push({s:a.id,t:'Fin',crit:t.crit&&t.EF===dur})})
  const paths:string[][]=[]
  const dfs=(u:string,p:string[])=>{if(u==='Fin'){paths.push(p);return}
    edges.filter(e=>e.crit&&e.s===u).forEach(e=>dfs(e.t,[...p,e.t]))}
  dfs('Inicio',['Inicio'])
  const cost=acts.reduce((s,a)=>s+a.c+slope(a)*(a.d-(cur[a.id]??a.d)),0)
  return{rows:order.map(i=>R.get(i)!),dur,cost,paths,edges,order}
}

// Aceleración automática: en cada paso reduce 1 unidad el conjunto de actividades críticas
// de menor coste que corta TODAS las rutas críticas; recalcula CPM tras cada reducción.
export function crash(acts:Act[],target:number){
  const cur:Record<string,number>=Object.fromEntries(acts.map(a=>[a.id,a.d]))
  const log:string[]=[]
  for(let it=0;it<500;it++){
    const r=cpm(acts,cur);if(r.dur<=target)break
    const cand=r.rows.filter(x=>x.crit&&cur[x.id]>x.dmin).slice(0,14)
    let best:{ids:string[];cost:number}|null=null
    for(let mask=1;mask<(1<<cand.length);mask++){
      const ids=cand.filter((_,i)=>mask>>i&1).map(x=>x.id)
      if(!r.paths.every(p=>ids.some(i=>p.includes(i))))continue
      const cost=ids.reduce((s,i)=>s+slope(acts.find(a=>a.id===i)!),0)
      if(!best||cost<best.cost||(cost===best.cost&&ids.length<best.ids.length))best={ids,cost}
    }
    if(!best){log.push('No es posible reducir más (límite de aceleración alcanzado).');break}
    best.ids.forEach(i=>cur[i]--)
    const n=cpm(acts,cur)
    log.push(`Duración ${r.dur} → ${n.dur}: acelerar ${best.ids.join(' + ')} (+${best.cost.toFixed(0)}/u). Rutas críticas: ${n.paths.length}`)
  }
  return{cur,log}
}
