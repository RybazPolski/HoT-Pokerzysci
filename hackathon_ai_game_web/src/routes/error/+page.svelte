<script>
    import Window from "$lib/components/Window.svelte";
</script>

<div class="flex w-screen bg-custom_white-500 mt-10 mb-10">

    <div class="w-2/12"></div>

    <div class="w-8/12">
        <div class="text-2xl mb-5">List of AI Agents/NPC</div>

        <Window>
            <div class="w-full h-96 flex flex-col gap-5  justify-center items-center">
                <img src="src/lib/images/icons8-error.gif" alt="Error Icon">
                <div class="text-2xl">Something went wrong!</div>

                <a href="/" class="py-2 px-4 bg-black text-white rounded">Go Back!</a>
            </div>
        </Window>
    </div>

    <div class="w-2/12"></div>


</div>
