<script lang="ts">
    import type { PageProps } from './$types';
    import {toast} from "svelte-sonner";
    import Window from "$lib/components/Window.svelte";
    import {onMount} from "svelte";
    import {supabase} from "$lib/helper/supabase";
    import {goto} from "$app/navigation";
    let { data }: PageProps = $props();

    let npcData = $state();

    let formData = {
        name: "",
        trait: "Argumentative",
        description: "",
        friendship: 0,
        address: ""
    };

    const traitList = [
        "Argumentative",
        "Arrogant",
        "Blustering",
        "Rude",
        "Curious",
        "Friendly",
        "Honest",
        "Hot tempered",
        "Irritable",
        "Ponderous",
        "Quiet",
        "Suspicious"

    ]


    onMount(async ()=>{

        if(!data){
            await goto("/error");
            return;
        }

        if(!data.hasOwnProperty("id")){
            await goto("/error");
            return;
        }

        if(!Number.isInteger(parseInt(data.id))){
            await goto("/error");
            return;
        }

        let id = parseInt(data.id);

        console.log(id)

        let { data: npc, error } = await supabase
            .from('npc')
            .select(`*`)
            .eq("id", id);

        console.log("Selected NPC:", npc);
        npcData = {...npc};
    });

    const handleSaveClick = () =>{

        toast("Changes were saved");
    }
</script>


<div class="flex w-screen mt-10">

    <div class="w-2/12"></div>

    <div class="w-8/12">
        <div class="text-2xl mb-5">NPC Parameters</div>

        <Window>
            <div class="w-full h-full">
                <form>
<!--                name-->
                <div class="flex flex-col gap-1">
                    <label for="npc_name">NPC name</label>
                    <input type="text" id="npc_name" bind:value={formData.name}
                           class="border border-gray-300 rounded-md p-1 indent-2 max-w-64 transition duration-300"
                           placeholder="name" />

                </div>

<!--                trait-->
                <div class="flex flex-col gap-1">
                    <label for="npc_trait">NPC trait</label>
                    <div class="relative max-w-64">
                        <select
                                bind:value={formData.trait}
                                class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded pl-3 pr-8 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-400 shadow-sm focus:shadow-md appearance-none cursor-pointer">
                            {#each traitList as trait}
                                <option value={trait}>{trait}</option>
                            {/each}
                        </select>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.2" stroke="currentColor" class="h-5 w-5 ml-1 absolute top-2.5 right-2.5 text-slate-700">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 15 12 18.75 15.75 15m-7.5-6L12 5.25 15.75 9" />
                        </svg>
                    </div>


                    <div class="flex flex-col gap-1">
                        <label for="npc_description">Description</label>
                        <textarea id="npc_description" bind:value={formData.description}
                                  class="border border-gray-300 rounded-md p-1 max-w-64"></textarea>
                    </div>

                    <div class="flex flex-col gap-1">
                        <label for="npc_friendship">Friendship Level</label>
                        <input type="number" id="npc_friendship" bind:value={formData.friendship}
                               class="border border-gray-300 rounded-md p-1 max-w-64" max="100" min="0" />
                    </div>

                    <div class="flex flex-col gap-1">
                        <label for="npc_address">Address</label>
                        <textarea id="npc_address" bind:value={formData.address}
                               class="border border-gray-300 rounded-md p-1 max-w-64" />
                    </div>
                </div>
                </form>
            </div>


            <button
                    onclick={()=>goto("/")}
                    class="absolute cursor-pointer bottom-5 right-24 bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                Cancel
            </button>

            <button
                    onclick={handleSaveClick}
                    class="absolute cursor-pointer bottom-5 right-5 bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
                Save
            </button>
        </Window>
    </div>

    <div class="w-2/12"></div>


</div>