<script>
    export let titles;
    export let agents;


</script>

<div class="">
    <div class="grid grid-cols-4 gap-4">
        {#each titles as title}
            <div class="font-bold p-2">{title}</div>
        {/each}
    </div>
    {#each agents as agent}
        <a class="grid grid-cols-4 gap-4 border-bottom border-b-[1px] border-gray-300 transition hover:bg-slate-100" href={`/${agent.id}`}>
            <div class="p-2">{agent.name}</div>
            <div class="p-2">{agent.created_at}</div>
            <div class="p-2">{agent.traits}</div>
        </a>
    {/each}
</div>